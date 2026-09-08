%undefine _debugsource_packages

%define major	2
%define oldlibname %mklibname cares 2
%define libname %mklibname cares
%define devname %mklibname cares -d

Summary:	A library that performs asynchronous DNS operations
Name:		c-ares
Version:	1.34.8
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://c-ares.haxx.se/
Source0:	https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz

BuildSystem:	cmake
BuildOption:	-DCARES_SYMBOL_HIDING:BOOL=ON

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

# DNS packet parse/build and query state machine have complex branching;
# ahost/adig on local names are a useful profile. No network required.
%pgo
_bd="$PWD/_OMV_rpm_build"
export LD_LIBRARY_PATH="$_bd${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
adig=
ahost=
for d in "$_bd" "$_bd/bin" "$_bd/src/tools" "$_bd/src"; do
	[ -x "$d/adig" ] && adig="$d/adig"
	[ -x "$ahost" ] || { [ -x "$d/ahost" ] && ahost="$d/ahost"; }
done
if [ -z "$adig" ] || [ -z "$ahost" ]; then
	echo "PGO: instrumented adig/ahost missing under $_bd" >&2
	find "$_bd" -name adig -o -name ahost 2>/dev/null || true
	exit 1
fi
"$adig" -h >/dev/null 2>&1 || true
"$ahost" -h >/dev/null 2>&1 || true
for n in localhost localhost.localdomain $(hostname) 127.0.0.1 ::1; do
	"$ahost" "$n" >/dev/null 2>&1 || true
	"$adig" "$n" >/dev/null 2>&1 || true
	"$adig" A "$n" >/dev/null 2>&1 || true
	"$adig" AAAA "$n" >/dev/null 2>&1 || true
	"$adig" PTR 1.0.0.127.in-addr.arpa >/dev/null 2>&1 || true
done
if [ -r /etc/hosts ]; then
	"$ahost" -f /etc/hosts localhost >/dev/null 2>&1 || true
fi

%files
%{_bindir}/adig
%{_bindir}/ahost
%{_mandir}/man1/adig.1*
%{_mandir}/man1/ahost.1*

%files -n %{libname}
%{_libdir}/libcares.so.%{major}*

%files -n %{devname}
%{_includedir}/ares*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libcares.pc
%{_libdir}/cmake/c-ares
%doc %{_mandir}/man3/ares_*
