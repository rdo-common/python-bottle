%global srcname bottle

Name:           python-%{srcname}
Version:        0.12.6
Release:        1%{?dist}
Summary:        Fast and simple WSGI-framework for small web-applications

Group:          Development/Languages
License:        MIT
URL:            http://bottlepy.org
Source0:        http://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Bottle is a fast and simple micro-framework for small web-applications. 
It offers request dispatching (Routes) with URL parameter support, Templates, 
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and 
template engines. All in a single file and with no dependencies other than the 
Python Standard Library.

%prep
%setup -q -n %{srcname}-%{version}
sed -i '/^#!/d' bottle.py


%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}%{_bindir}/bottle.py

%files
%doc README.rst PKG-INFO
%{python_sitelib}/*

%changelog
* Fri Feb 20 2015 Michel Samia <msamia@netsuite.com> - 0.12.6-1
- populated new el6 branch from master
- removed python3 parts as it isn't in el6

* Sat Jul 12 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.12.6-1
- resolves rhbz#1093257 - JSON content type not restrictive enough

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.11.6-1
- upstream release 0.11.6
- add python3 subpackage. resolves rhbz#949240
- spec file patch from Haïkel Guémar <hguemar@fedoraproject.org>

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Ian Weller <iweller@redhat.com> - 0.10.7-1
- Update to 0.10.7 (required by python-mwlib)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.5-1
- Initial spec
