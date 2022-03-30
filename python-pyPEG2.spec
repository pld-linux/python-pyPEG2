#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An intrinsic PEG Parser-Interpreter for Python
Name:		python-pyPEG2
Version:	2.15.2
Release:	6
License:	GPLv2+
Group:		Libraries/Python
Source0:	http://fdik.org/pyPEG2/pyPEG2-%{version}.tar.gz
# Source0-md5:	2ff44bc843c61ccd3951ef66a9e4a2b0
URL:		http://fdik.org/pyPEG2
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An intrinsic PEG Parser-Interpreter for Python.

%package -n python3-pyPEG2
Summary:	Python 3 bindings for an intrinsic PEG Parser-Interpreter for Python
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pyPEG2
An intrinsic PEG Parser-Interpreter for Python.

%prep
%setup -q -n pyPEG2-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt TODO.txt
%{py_sitescriptdir}/pypeg2
%{py_sitescriptdir}/pyPEG2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyPEG2
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt TODO.txt
%{py3_sitescriptdir}/pypeg2
%{py3_sitescriptdir}/pyPEG2-%{version}-py*.egg-info
%endif
