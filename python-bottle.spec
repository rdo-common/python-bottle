%global srcname bottle
Name:           python-%{srcname}
Version:        0.9.5
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
It offers request dispatching (Routes) with url parameter support, Templates, 
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and 
template engines. All in a single file and with no dependencies other than the 
Python Standard Library.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE.txt PKG-INFO
%{python_sitelib}/%{srcname}.py*
%{python_sitelib}/%{srcname}*.egg-info

%changelog
* Mon Jul 18 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.5-1
- Initial spec
