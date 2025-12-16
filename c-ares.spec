%undefine _debugsource_packages

%define major	2
%define oldlibname %mklibname cares 2
%define libname %mklibname cares
%define devname %mklibname cares -d

Summary:	A library that performs asynchronous DNS operations
Name:		c-ares
Version:	1.34.6
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://c-ares.haxx.se/
Source0:	https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz

%description
c-ares is a C library that performs DNS requests and name resolves 
asynchronously. c-ares is a fork of the library named 'ares', written 
by Greg Hudson at MIT.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name} = %{version}-%{release}
%rename %{oldlibname}

%description -n %{libname}
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n %{devname}
Summary:	Development files for c-ares
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and developemnt libraries
needed to compile applications or shared objects that use c-ares.

%prep
%autosetup -p1

%build
export LDFLAGS=$(echo %ldflags | sed -e 's/-D_FORTIFY_SOURCE=2//')
export CFLAGS=$(echo %optflags | sed -e 's/-D_FORTIFY_SOURCE=2//')
%configure \
	--enable-shared \
	--enable-thread \
	--enable-libgcc \
	--enable-nonblocking \
	--enable-optimize \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libcares.so.%{major}*

%files -n %{devname}
%{_includedir}/ares*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libcares.pc
%doc %{_mandir}/man3/ares_*
