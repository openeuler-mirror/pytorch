%global _empty_manifest_terminate_build 0
Name:		pytorch
Version:	1.6.0
Release:	2
Summary:	Tensors and Dynamic neural networks in Python with strong GPU acceleration
License:	BSD-3
URL:		https://pytorch.org/
#sh -x updateSource.sh
Source0:	pytorch-%{version}-include-submodules.tar.bz2

Patch0001:	0001-Fix-illegal-opcode-bug-in-caffe2-40584.patch
Patch0002:	0002-disable-SVE-for-v1.6.0-due-to-sleef-build-error.patch

Requires:	python3-future
Requires:	python3-numpy

%description
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system
You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend PyTorch when needed.

%package -n python3-pytorch
Summary:	Tensors and Dynamic neural networks in Python with strong GPU acceleration
Provides:	python-torch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pyyaml
BuildRequires:	cmake
BuildRequires:	python3-numpy

%description -n python3-pytorch
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system
You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend PyTorch when needed.

%package help
Summary:	Development documents and examples for torch
Provides:	python3-pytorch-doc
%description help
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system
You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend PyTorch when needed.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-pytorch -f filelist.lst
%dir %{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Feb 4 2021 Zhipeng Xie<xiezhipeng1@huawei.com> - 1.6.0-2
- disable SVE to fix compile error in gcc 9

* Sun Sep 27 2020 Zhipeng Xie<xiezhipeng1@huawei.com> - 1.6.0-1
- Package init
