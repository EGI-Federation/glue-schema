# README for glue-schema package

Home for the GLUE Specification:
[OGF Forge](http://forge.ogf.org/sf/projects/glue-wg).

Documentation: [readthedocs](http://gridinfo-documentation.readthedocs.io).

## Installing from packages

### On RHEL-based systems

On RHEL-based systems, it's possible to install packages from EPEL or
[EGI UMD packages](https://go.egi.eu/umd).

The UMD packages are built automatically from this repository, and tested to
work with other components part of the Unified Middleware Distribution.

## Building packages

A Makefile allowing to build source tarball and packages is provided.

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```shell
# Checkout tag to be packaged
$ git clone https://github.com/EGI-Foundation/glue-schema.git
$ cd glue-schema
$ git checkout X.X.X
# Building in a container
$ docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
[root@8a9d60c61f42 /]# cd /source
[root@8a9d60c61f42 /]# yum install -y rpm-build yum-utils
[root@8a9d60c61f42 /]# yum-builddep -y glue-schema.spec
[root@8a9d60c61f42 /]# make rpm
```

The RPM will be available into the `build/RPMS` directory.

### Building a deb

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/glue-schema.git
cd glue-schema
git checkout X.X.X
# Building in a container using the source files
docker run --rm -v $(pwd):/source -it ubuntu:latest
apt update
apt install -y devscripts debhelper make rsync
cd /source && make deb
```

The DEB will be available into the `build/` directory.

## Installing from source

This procedure is not recommended for production deployment, please consider
using packages.

- Build dependencies: None
- Runtime dependencies: openldap

Get the source by cloning this repository and do a `make install`.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in
    - [CHANGELOG](CHANGELOG)
    - [glue-schema.spec](glue-schema.spec)
    - [debian/changelog](debian/changelog)
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
