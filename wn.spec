%global debug_package %{nil}

Name: wn
Version: 5.0.0
Release: 1%{?dist}
Summary: Worker Node meta-package
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/EGI-Federation/wn-metapackage
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build

Requires: c-ares
Requires: dcap
Requires: dcap-devel
Requires: dcap-libs
Requires: dcap-tunnel-gsi
Requires: dcap-tunnel-krb
Requires: dcap-tunnel-ssl
Requires: dcap-tunnel-telnet
%if 0%{?rhel} == 7
Requires: cvmfs
Requires: cleanup-grid-accounts
Requires: dcache-srmclient
Requires: dpm
Requires: libdpm.so.1()(64bit),  dpm-libs
Requires: dpm-devel
Requires: dpm-perl
Requires: dpm-python
Requires: gfalFS
Requires: ginfo
Requires: lcg-info
Requires: lcg-infosites
Requires: lcg-ManageVOTag
Requires: lcg-tags
Requires: lcgdm-devel
Requires: glite-yaim-core
Requires: lfc
Requires: lfc-devel
Requires: lfc-perl
Requires: liblfc.so.1()(64bit), lfc-libs
%endif
Requires: fetch-crl
Requires: gfal2-all
Requires: gfal2-all
%if 0%{?rhel} == 7
Requires: gfal2-python
%else
Requires: gfal2-python3
%endif
Requires: gfal2-all
Requires: gfal2-doc
Requires: gfal2-devel
Requires: globus-gass-copy-progs
Requires: globus-proxy-utils
Requires: gridsite-libs
Requires: openldap-clients
Requires: python-ldap
Requires: uberftp
Requires: voms-clients-java
Requires: voms-devel
Requires: xrootd-client

%description
List of WN dependencies (APIs & clients).

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc /usr/share/doc/wn/README.md

%changelog
* Tue Jun 04 2024 Andrea Manzi <andrea.manzi@egi.eu> - 5.0.0-1
- Add support for EL9
* Thu Jun 01 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.5-1
- renamed to wn
* Wed May 24 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.4-1
- removed glite-lb-client-progs and deps, added xrootd-client
* Thu Mar 30 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.3-1
- added glite-yaim-core and cvmfs
* Thu Mar 09 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.2-1
- removed umd-release packages as they contain the UMD repos
- added glite-lb-client-progs and deps
* Wed Feb 01 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.1-1
- added dcache-srm-client and umd-release packages to C7
* Mon Sep 05 2016 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.0-1
- first build for C7
- remove SL5 support
* Sun Sep 07 2014 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.1.0-1
- added dependecies on gfal2-util and ginfo (IGIRTC-176)
* Mon Sep 09 2013 Adrien Devresse <adevress at cern.ch> - 3.0.2-2
- fix for lcgdm-devel 32 bits dependency problem on EL5
* Thu Feb 14 2013 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.0.0-1
- added gfal2-doc and gfal2-devel
* Thu Oct 11 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.1-1
- passing to the final versioning
* Fri Oct 05 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-4
- Updated deps according to DM Integration/Clients
* Fri Aug 31 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-3
- Added missing dependencis to the EMI 2 version (includes 32b)
* Fri Apr 01 2011 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 1.0.0-0
- First version for EMI
