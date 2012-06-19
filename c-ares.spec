%define major 2
%define libname %mklibname cares %{major}
%define libdevelname %mklibname cares -d
%define libstaticname %mklibname cares -d -s

Summary:	A library that performs asynchronous DNS operations
Name:		c-ares
Version:	1.9.1
Release:	1
License:	MIT
Group:		System/Libraries
URL:		http://c-ares.haxx.se/
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

%package -n %{libdevelname}
Summary:	Development files for c-ares
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{libdevelname}
This package contains the header files and developemnt libraries
needed to compile applications or shared objects that use c-ares.

%package -n %{libstaticname}
Summary:	Static development library for c-ares
Group:		Development/C
Requires:	%{libdevelname} = %{version}-%{release}

%description -n	%{libstaticname}
This package contains the static development library for c-ares
needed to compile applications using c-ares.

%prep
%setup -q

%build
%configure2_5x	\
	--enable-shared \
	--enable-thread \
	--enable-libgcc \
	--enable-nonblocking \
	--enable-optimize

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{libdevelname}
%doc README README.cares CHANGES NEWS
%{_includedir}/ares*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*

%files -n %{libstaticname}
%{_libdir}/lib*.a
