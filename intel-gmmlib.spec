Summary:	Intel Graphics Memory Management Library
Name:		intel-gmmlib
Version:	19.2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/intel/gmmlib/archive/%{name}-%{version}/intel-gmmlib-%{version}.tar.gz
# Source0-md5:	4004db0e2efcff2d2b3702f59c8ce0b2
URL:		https://github.com/intel/gmmlib/
BuildRequires:	cmake >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for
OpenCL and the Intel Media Driver for VAAPI.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -qn gmmlib-%{name}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libigdgmm.so.9.*.*
%ghost %attr(755,root,root) %{_libdir}/libigdgmm.so.9

%files devel
%defattr(644,root,root,755)
%{_includedir}/igdgmm
%attr(755,root,root) %{_libdir}/libigdgmm.so
%{_pkgconfigdir}/igdgmm.pc
