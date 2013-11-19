Summary:	Stand-alone template engine written in Python
Name:		python-Jinja2
Version:	2.7.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
# Source0-md5:	282aed153e69f970d6e76f78ed9d027a
URL:		http://jinja.pocoo.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jinja2 is a template engine written in pure Python. It provides
a Django inspired non-XML syntax but supports inline expressions
and an optional sandboxed environment.

%prep
%setup -qn Jinja2-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py_sitescriptdir}/jinja2
%{py_sitescriptdir}/*.egg-info

