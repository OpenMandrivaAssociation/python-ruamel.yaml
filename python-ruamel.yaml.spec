%define _empty_manifest_terminate_build 0

Summary:	Python library for loading and dumping YAML 1.2
Name:		python-ruamel.yaml
Version:	0.17.10
Release:	3
Group:		Development/Python
License:	BSD
Url:		https://pypi.org/project/ruamel.yaml/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml/ruamel.yaml-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(wheel)

%description
Python library for loading and dumping YAML 1.2

%files
%{py_puresitedir}/ruamel
%{py_puresitedir}/ruamel.yaml*.dist-info
%{py_puresitedir}/*.pth
#{py_platsitedir}/ruamel.yaml.clib*
#{py_platsitedir}/_ruamel_yaml*.so

#------------------------------------------------------------
%prep
%autosetup -p1 -n ruamel.yaml-%{version}

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
pip \
	install \
	--root="%{buildroot}" .

%check
%{__python} setup.py \
	check
