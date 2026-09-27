import pathlib
import subprocess
import unittest


class NetworkConfigTest(unittest.TestCase):
    def test_netfs_support_matches_kernel_version(self):
        workflow = pathlib.Path(__file__).parent / ".github/workflows/build.yml"
        source = workflow.read_text()
        block = source.split("          # CIFS 网络文件系统", 1)[1].split("\n", 1)[1].split("          # 6.12 的 NETFS", 1)[0]
        for version, expected in (("5.10", False), ("5.15", True), ("6.1", False), ("6.6", True), ("6.12", True)):
            with self.subTest(version=version):
                result = subprocess.run(
                    ["bash", "-e", "-c", 'set_config() { printf "%s=%s\\n" "$1" "$2"; }; ' + block],
                    env={"KVER": version, "PATH": "/usr/bin:/bin"},
                    text=True,
                    capture_output=True,
                    check=True,
                )
                self.assertEqual("CONFIG_NETFS_SUPPORT=y" in result.stdout.splitlines(), expected)


if __name__ == "__main__":
    unittest.main()
