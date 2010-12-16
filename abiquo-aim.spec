Name:           abiquo-aim
BuildRequires:  hiredis gcc-c++ thrift-cpp-devel boost-devel curl-devel libvirt-devel 
Requires:	libvirt hiredis boost
Version:        1.7.0
Release:        1.rel1.1
Url:            http://www.abiquo.com/
License:        BSD(or similar)
Group:          System/Management
Summary:        Abiquo Cloud Node Agent
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source1:	abiquo-aim.ini
Source2:	abiquo-aim.init

%description
Summary:        Abiquo Cloud Node Agent


Authors:
--------
    Abiquo Development Team

%prep
%setup -q

%build
CPATH="/usr/include/thrift:/usr/include/hiredis" make

%install
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d
cp $RPM_BUILD_DIR/%{name}-%{version}/src/aim $RPM_BUILD_ROOT/%{_sbindir}/abiquo-aim
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/abiquo-aim.ini
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/abiquo-aim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/abiquo-aim
%config(noreplace) %{_sysconfdir}/abiquo-aim.ini
%{_sysconfdir}/rc.d/init.d/abiquo-aim

%post
/sbin/chkconfig --add abiquo-aim
if ! [ -d /var/lib/virt ]; then
	mkdir -p /var/lib/virt 
fi
if ! [ -d /opt/vm_repository ]; then
	mkdir -p /opt/vm_repository
fi

%changelog
* Thu Dec 16 2010 Sergio Rubio <srubio@abiquo.com> - 1.7.0-1.rel1.1
- updated to upstream 1.7.0

* Thu Sep 16 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-2.rel1.1
- Updated default config

* Thu Sep 16 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1.rel1.1
- Updated to upstream 1.1

* Thu Sep 16 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-8.rel1.0
- Updated aim init script

* Fri Sep 10 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-7.rel1.0
- Update aim source

* Thu Sep 09 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-6
- create required dirs in post
- fixes to the init script

* Thu Sep 09 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-5
- Require boost

* Thu Sep 09 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-4
- Do not replace aim config

* Thu Sep 09 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-3
- Added config file
- Added init script

* Thu Sep 09 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-2
- Fixed deps

* Thu Sep 09 2010 Sergio Rubio <srubio@abiquo.com> 1.6.5-1
- Initial Release
