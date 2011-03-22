Name:           glue-schema
Version:        2.0.7
Release:        1%{?dist}
Summary:        LDAP schema files for the GLUE Schema
Group:          Development/Tools
License:        ASL 2.0
URL:            http://forge.ogf.org/sf/projects/glue-wg
#               wget -O %{name}-%{version}.tar.gz "http://svnweb.cern.ch/world/wsvn/gridinfo/glue-schema/tags/R_2_0_6/?op=dl"
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
LDAP schema files for the GLUE Schema version 2.0

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
* Tue Mar 22 2011 Laurence Field <laurence.field@cern.ch> -  2.0.7-1
- Derived FKs are now optional
* Fri Jun 25 2010 Daniel Johansson <daniel@nsc.liu.se> - 2.0.6-1
- Updated Licences
* Thu Feb 25 2010 Daniel Johansson <daniel@nsc.liu.se> - 2.0.3-1
- Updated packaging
* Fri Jul 10 2009 Laurence Field <laurence.field@cern.ch> -  2.0.1-1
- First release
