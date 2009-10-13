# TODO:
# upstream: add licensing file (and confirm the one configurated here)
# upstream: add some README file

Name:           glue-schema
Version:        2.0.3
Release:        1%{?dist}
Summary:        LDAP schema files for the GLUE Schema
Group:          Development/Tools
#License:        Open Grid Forum Full Copyright Notice
License:        Copyright only
URL:            https://svnweb.cern.ch/trac/gridinfo/browser/glue-schema/
#URL:            http://forge.gridforum.org/sf/projects/glue-wg
Source0:        http://glue.web.cern.ch/glue/glue-schema-%{version}.src.tgz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
LDAP schema file for the GLUE Schema version 2.0

%prep
%setup -q -c

%build 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/ldap/schema/
install etc/ldap/schema/* %{buildroot}/%{_sysconfdir}/ldap/schema/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ldap/schema/*

%doc

%changelog
* Fri Jul 10 2009 Laurence Field <laurence.field@cern.ch> -  2.0.1-1
- First release

