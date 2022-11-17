# Worker Node WN) metapackage

WN dependencies (APIs & clients), to deploy a Worker Node (WN) for
[High Throughput Compute](https://docs.egi.eu/users/compute/high-throughput-compute/).

The package relies on packages available in the following repositories:

- [UMD](https://repository.egi.eu/)
- [EPEL](https://docs.fedoraproject.org/en-US/epel/)

## Building packages

### Building the RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```shell
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/wn-metapackage.git
cd wn-metapackage
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `wn.spec`
  - Updating version and changelog in `CHANGELOG`
- Once the PR has been merged, publish a new release using GitHub web interface
  - Suffix the tag name to be created with `v`, like `v1.0.0`
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project. This is now hosted here on GitHub, and
maintained by the EGI Federation.
