%define	debug_package %{nil}

%define major	2
%define libname %mklibname cares %{major}
%define devname %mklibname cares -d

Summary:	A library that performs asynchronous DNS operations
Name:		c-ares
Version:	1.13.0
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://c-ares.haxx.se/
Source0:	http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz

%description
c-ares is a C library that performs DNS requests and name resolves 
asynchronously. c-ares is a fork of the library named 'ares', written 
by Greg Hudson at MIT.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name} = %{version}-%{release}

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
%setup -q
%build
export LDFLAGS=`echo %ldflags | sed -e 's/-D_FORTIFY_SOURCE=2//'`
export CFLAGS=`echo %optflags | sed -e 's/-D_FORTIFY_SOURCE=2//'`
%configure \
	--enable-shared \
	--enable-thread \
	--enable-libgcc \
	--enable-nonblocking \
	--enable-optimize \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libcares.so.%{major}*

%files -n %{devname}
%doc README.cares CHANGES NEWS
%{_includedir}/ares*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*

