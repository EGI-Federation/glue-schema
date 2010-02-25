# TODO:
# upstream: add licensing file (and confirm the one configurated here)
# upstream: add some README file

Name:           glue-schema
Version:        2.0.3
Release:        1%{?dist}
Summary:        LDAP schema files for the GLUE Schema
Group:          Development/Tools
#               The INFN license is BSD with advertising
#               Open Grid Forum Full Copyright Notice
License:        BSD with advertising and Copyright only
URL:            https://svnweb.cern.ch/trac/gridinfo/browser/glue-schema/
#               wget -O %{name}-%{version}.tar.gz "http://svnweb.cern.ch/world/wsvn/gridinfo/glue-schema/tags/R_2_0_3/?op=dl"
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
LDAP schema file for the GLUE Schema version 2.0

%prep
%setup -q
# Change to the one below if you are building against downloaded tarball from svnweb.cern.ch
#%setup -q -n R_2_0_3.r97

%build 
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/ldap/schema/
install -m 644 etc/ldap/schema/* %{buildroot}/%{_sysconfdir}/ldap/schema/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/ldap
%doc

%changelog
* Thu Feb 25 2010 Daniel Johansson <daniel@nsc.liu.se> - 2.0.3-1
- Updated packaging
* Fri Feb 12 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-1
- Updated packaging
* Fri Jul 10 2009 Laurence Field <laurence.field@cern.ch> -  2.0.1-1
- First release

