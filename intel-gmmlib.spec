Summary:	Intel Graphics Memory Management Library
Summary(pl.UTF-8):	Biblioteka zarządzania pamięcią kart graficznych Intela
Name:		intel-gmmlib
Version:	22.8.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/intel/gmmlib/tags
Source0:	https://github.com/intel/gmmlib/archive/%{name}-%{version}/intel-gmmlib-%{version}.tar.gz
# Source0-md5:	e43198dee270a7accad3d39e2385ed9b
URL:		https://github.com/intel/gmmlib/
BuildRequires:	cmake >= 3.5
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for
OpenCL and the Intel Media Driver for VAAPI.

%description -l pl.UTF-8
Bibliotek Intel Graphics Memory Management zapewnia zależne od
urządzenia zarządzanie buforami dla bibliotek Intel Graphics Compute
Runtime na potrzeby OpenCL oraz sterownika Intel Media Driver dla
VAAPI.

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
%attr(755,root,root) %{_libdir}/libigdgmm.so.12.*.*
%ghost %{_libdir}/libigdgmm.so.12

%files devel
%defattr(644,root,root,755)
%{_libdir}/libigdgmm.so
%{_includedir}/igdgmm
%{_pkgconfigdir}/igdgmm.pc
