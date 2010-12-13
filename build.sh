SIGN_PKGS=0
AIM_VERSION=1.6.8
MOCK_PROFILE=abiquo-1.6.8
PKG_NAME=abiquo-aim
TARBALL_URL=http://10.60.1.87/1.6.8-SNAPSHOT/premium/abiquo-aim-$AIM_VERSION.tar.bz2
BUILDBASE=~/rpmbuild

wget $TARBALL_URL -O - > abiquo-aim-$AIM_VERSION.tar.bz2
source ~/Work/rpmdev/build.sh
