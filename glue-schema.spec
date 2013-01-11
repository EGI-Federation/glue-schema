Name:           glue-schema
Version:        2.0.10
Release:        1%{?dist}
Summary:        LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema
Group:          Development/Tools
License:        ASL 2.0
URL:            http://forge.ogf.org/sf/projects/glue-wg
#               wget -O %{name}-%{version}.tar.gz "http://svnweb.cern.ch/world/wsvn/gridinfo/glue-schema/tags/R_2_0_10_1/?op=dl"
Source:         %{name}-%{version}.src.tgz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema

%prep
%setup -q
# Change to the one below if you are building against downloaded tarball from svnweb.cern.ch
#%setup -q -n R_2_0_3.r97

%build 
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/ldap/schema
install -m 644 -p etc/ldap/schema/* %{buildroot}/%{_sysconfdir}/ldap/schema

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/ldap
%doc debian/copyright

%changelog
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
