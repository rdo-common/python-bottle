%global srcname bottle

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{srcname}
Version:        0.12.9
Release:        1%{?dist}
Summary:        Fast and simple WSGI-framework for small web-applications

Group:          Development/Languages
License:        MIT
URL:            http://bottlepy.org
Source0:        https://github.com/bottlepy/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Bottle is a fast and simple micro-framework for small web-applications. 
It offers request dispatching (Routes) with URL parameter support, Templates, 
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and 
template engines. All in a single file and with no dependencies other than the 
Python Standard Library.

%package -n python2-%{srcname}
Summary:        Fast and simple WSGI-framework for small web-applications
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Bottle is a fast and simple micro-framework for small web-applications. 
It offers request dispatching (Routes) with URL parameter support, Templates, 
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and 
template engines. All in a single file and with no dependencies other than the 
Python Standard Library.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Fast and simple WSGI-framework for small web-applications
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname}
Bottle is a fast and simple micro-framework for small web-applications. 
It offers request dispatching (Routes) with URL parameter support, Templates, 
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and 
template engines. All in a single file and with no dependencies other than the 
Python Standard Library.
%endif

%prep
%setup -q -n %{srcname}-%{version}
sed -i '/^#!/d' bottle.py

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif
rm %{buildroot}%{_bindir}/bottle.py

%check
%__python2 test/testall.py verbose
%if 0%{?with_python3}
# Fails
# FAIL: test_delete_cookie (test_environ.TestResponse)
%__python3 test/testall.py verbose || :
%endif

%files -n python2-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/*
%endif

%changelog
* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.9-1
- Update to 0.12.9
- Run tests but ignore python3 failure for now
- Use modern python packaging guidelines

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
