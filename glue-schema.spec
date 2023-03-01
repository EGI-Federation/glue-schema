Name:           glue-schema
Version:        2.1.0
Release:        1%{?dist}
Summary:        LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema
Group:          Development/Tools
License:        ASL 2.0
URL:            https://github.com/EGI-Federation/glue-schema
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: rsync
BuildRequires: make
Requires: openldap-servers

%description
LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema

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
%config(noreplace) %{_sysconfdir}/ldap
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license %{_datadir}/licenses/%{name}-%{version}/COPYRIGHT
%license %{_datadir}/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Tue Jan 10 2023 Baptiste Grenier <baptiste.greneir@egi.eu> - 2.1.0-1
- Build packages for CentOS 7, Stream 8 and Stream 9 (#4) (Baptiste Grenier)
- Lint and build with GitHub Actions, add community files (#3) (Andrea Manzi)

* Wed Aug 06 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.11-1
- #GRIDINFO-53: All the entities but Entity moved to type STRUCTURAL
- #GRIDINFO-9: GLUE 2 booleans should be DirectoryString not LDAP boolean

* Fri Jan 11 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.10-1
- Define GLUE2GroupID as first name for the GLUE2Group object to be backwards compatible with previous BDII versions

* Wed Nov 21 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.9-1
- BUG #97717: DIT and Schema changes requested by ARC

* Wed Jul 18 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.8-2
- BUG 95044: Improved summary and description to describe that both glue 1.3 and glue 2.0 

* Wed Jul 13 2011 Laurence Field <laurence.field@cern.ch> -  2.0.8-1
- Addressed #84300 (Merged ARC and gLite MDS schema)

* Tue Mar 22 2011 Laurence Field <laurence.field@cern.ch> -  2.0.7-1
- Derived FKs are now optional

* Fri Jun 25 2010 Daniel Johansson <daniel@nsc.liu.se> - 2.0.6-1
- Updated Licences

* Thu Feb 25 2010 Daniel Johansson <daniel@nsc.liu.se> - 2.0.3-1
- Updated packaging

* Fri Jul 10 2009 Laurence Field <laurence.field@cern.ch> -  2.0.1-1
- First release
