# README for glue-schema package

Home for the GLUE Specification: http://forge.ogf.org/sf/projects/glue-wg

Documentation: http://gridinfo-documentation.readthedocs.io

## Installing from source

```sh
make install
```

- Build dependencies: None
- Runtime dependencies: openldap

## Building packages

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync
- systemd-rpm-macros, for RHEL >= 8

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/bdii.git
cd bdii
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

### Building a deb

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/bdii.git
cd bdii
git checkout X.X.X
# Building in a container using the source files
docker run --rm -v $(pwd):/source -it ubuntu:xenial
apt update
apt install -y devscripts debhelper make rsync python-all-dev
cd /source && make deb
```

The DEB will be available into the `build/` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `glue-schema.spec`
  - Updating version and changelog in `debian/changelog`
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using Travis and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
