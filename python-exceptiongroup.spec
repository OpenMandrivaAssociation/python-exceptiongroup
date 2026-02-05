%define module exceptiongroup
%bcond tests 1

Name:		python-exceptiongroup
Version:	1.3.1
Release:	1
License:	MIT AND Python-2.0
Summary:	Backport of PEP 654 (exception groups)
Group:		Development/Python
URL:		https://github.com/agronholm/exceptiongroup
Source0:	https://files.pythonhosted.org/packages/source/e/exceptiongroup/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(flit-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Backport of PEP 654 (exception groups)
This is a backport of the BaseExceptionGroup and ExceptionGroup classes from
Python 3.11.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -v
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
