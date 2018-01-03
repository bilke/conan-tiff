from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(archs = ["x86_64"], args="--build=missing")
    builder.add_common_builds()
    builder.run()
