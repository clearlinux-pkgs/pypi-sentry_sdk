#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sentry_sdk
Version  : 1.5.9
Release  : 12
URL      : https://files.pythonhosted.org/packages/2b/a6/acafd704b17e72708c384db9b907a5c7e76ef89031ad92883e6983069098/sentry-sdk-1.5.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/a6/acafd704b17e72708c384db9b907a5c7e76ef89031ad92883e6983069098/sentry-sdk-1.5.9.tar.gz
Summary  : Python client for Sentry (https://sentry.io)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-sentry_sdk-license = %{version}-%{release}
Requires: pypi-sentry_sdk-python = %{version}-%{release}
Requires: pypi-sentry_sdk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(certifi)
BuildRequires : pypi(urllib3)

%description
<p align="center">
<a href="https://sentry.io" target="_blank" align="center">
<img src="https://sentry-brand.storage.googleapis.com/sentry-logo-black.png" width="280">
</a>
</p>

%package license
Summary: license components for the pypi-sentry_sdk package.
Group: Default

%description license
license components for the pypi-sentry_sdk package.


%package python
Summary: python components for the pypi-sentry_sdk package.
Group: Default
Requires: pypi-sentry_sdk-python3 = %{version}-%{release}

%description python
python components for the pypi-sentry_sdk package.


%package python3
Summary: python3 components for the pypi-sentry_sdk package.
Group: Default
Requires: python3-core
Provides: pypi(sentry_sdk)
Requires: pypi(certifi)
Requires: pypi(urllib3)

%description python3
python3 components for the pypi-sentry_sdk package.


%prep
%setup -q -n sentry-sdk-1.5.9
cd %{_builddir}/sentry-sdk-1.5.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649690640
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sentry_sdk
cp %{_builddir}/sentry-sdk-1.5.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sentry_sdk/3e100b2f32e3b106d00353c68b24a2e3c70adf79
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sentry_sdk/3e100b2f32e3b106d00353c68b24a2e3c70adf79

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
