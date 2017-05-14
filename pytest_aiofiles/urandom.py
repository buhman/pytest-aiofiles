import os

from pyfakefs import fake_filesystem


class FakeOsModule(fake_filesystem.FakeOsModule):
    real_open = os.open

    def open(self, file_path, flags, mode=None):
        if file_path == '/dev/urandom':
            return self.real_open(file_path, flags, mode)

        return super().open(file_path, flags, mode)


class FakeFileOpen(fake_filesystem.FakeFileOpen):
    real_open = open

    def Call(self, file_path, *args, **kwargs):  # noqa: N802
        if file_path == '/dev/urandom':
            return self.real_open(file_path, *args, **kwargs)

        return super().Call(file_path, *args, **kwargs)
