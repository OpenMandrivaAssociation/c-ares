%define	major	2
%define	libname	%mklibname cares %{major}
%define	libdev	%mklibname cares -d
%define	libstat	%mklibname cares -d -s

Summary:	A library that performs asynchronous DNS operations
Name:		c-ares
Version:	1.5.2
Release:	%mkrel 1
License:	MIT
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://daniel.haxx.se/projects/c-ares/
Source0:	http://daniel.haxx.se/projects/c-ares/c-ares-%{version}.tar.gz

%description
c-ares is a C library that performs DNS requests and name resolves 
asynchronously. c-ares is a fork of the library named 'ares', written 
by Greg Hudson at MIT.

%package -n	%{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n	%{libdev}
Summary:	Development files for c-ares
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libdev}
This package contains the header files and developemnt libraries
needed to compile applications or shared objects that use c-ares.

%package -n	%{libstat}
Summary:	Static development library for c-ares
Group:		%{group}
Requires:	%{libdev} = %{version}

%description -n	%{libstat}
This package contains the static development library for c-ares
needed to compile applications using c-ares.

%prep
%setup -q

%build
%configure2_5x	--enable-shared
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{libdev}
%doc README README.cares CHANGES NEWS
%{_includedir}/ares.h
%{_includedir}/ares_dns.h
%{_includedir}/ares_version.h
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*

%files -n %{libstat}
%{_libdir}/lib*.a
