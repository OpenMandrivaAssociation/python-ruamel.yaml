%undefine _debugsource_packages

Summary:	Python library for loading and dumping YAML 1.2
Name:		python-ruamel.yaml
Version:	0.18.16
Release:	1
Group:		Development/Python
License:	BSD
Url:		https://pypi.org/project/ruamel.yaml/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml/ruamel.yaml-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Python library for loading and dumping YAML 1.2

%files
%{py_puresitedir}/ruamel
%{py_puresitedir}/ruamel_yaml-%{version}.dist-info
#{py_puresitedir}/*.pth
#{py_platsitedir}/ruamel.yaml.clib*
#{py_platsitedir}/_ruamel_yaml*.so
