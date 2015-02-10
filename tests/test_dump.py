import tempfile

import numpy

from examples.sqrt import main as sqrt_example
from blocks.dump import MainLoopDumpManager


def test_main_loop_state_manager():
    def assert_equal(main_loop1, main_loop2, check_log=True):
        """Check if two main loop objects are equal.

        Notes
        -----
        Corrupts the iteration state!

        """
        W1 = (main_loop1.model.linear_transformations[0]
                              .params[0].get_value())
        W2 = (main_loop2.model.linear_transformations[0]
                              .params[0].get_value())
        assert numpy.all(W1 == W2)
        if check_log:
            assert sorted(list(main_loop1.log)) == sorted(list(main_loop2.log))
        assert numpy.all(
            next(main_loop1.epoch_iterator)["numbers"] ==
            next(main_loop2.epoch_iterator)["numbers"])

    folder = tempfile.mkdtemp()
    folder2 = tempfile.mkdtemp()

    main_loop1 = sqrt_example(folder, 17)
    assert main_loop1.log.status.epochs_done == 3
    assert main_loop1.log.status.iterations_done == 17

    # Test loading from the folder where `main_loop` is saved
    main_loop2 = sqrt_example(folder2, 1)
    manager = MainLoopDumpManager(folder)
    manager.load_to(main_loop2)
    assert_equal(main_loop1, main_loop2)

    # Reload because `main_loop2` is corrupted by `assert_equal`
    main_loop2 = sqrt_example(folder2, 1)
    manager.load_to(main_loop2)
    # Continue until 33 iterations are done
    main_loop2.find_extension("FinishAfter").set_conditions(after_n_batches=33)
    main_loop2.run()
    assert main_loop2.log.status.iterations_done == 33

    # Compare with a main loop after continuous 33 iterations
    main_loop3 = sqrt_example(folder, 33)
    assert main_loop3.log.status.iterations_done == 33
    assert_equal(main_loop2, main_loop3, check_log=False)
