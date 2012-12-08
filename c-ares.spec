%define major 2
%define libname %mklibname cares %{major}
%define libdevelname %mklibname cares -d

Summary:	A library that performs asynchronous DNS operations
Name:		c-ares
Version:	1.9.1
Release:	2
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
Obsoletes:	%{mklibname cares -d -s} < %{version}-%{release}

%description -n	%{libdevelname}
This package contains the header files and developemnt libraries
needed to compile applications or shared objects that use c-ares.

%prep
%setup -q

%build
%configure2_5x	\
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
%{_libdir}/lib*.so.%{major}*

%files -n %{libdevelname}
%doc README README.cares CHANGES NEWS
%{_includedir}/ares*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*


%changelog
* Wed Jun 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.9.1-1
+ Revision: 806303
- version update 1.9.1

* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.8.0-1
+ Revision: 794266
- version update 1.8.0

* Thu Aug 25 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.5-1
+ Revision: 697071
- update to new version 1.7.5

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.4-2
+ Revision: 663346
- mass rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.4-1
+ Revision: 633067
- update to new version 1.7.4

* Sat Jul 10 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.3-1mdv2011.0
+ Revision: 550110
- update to new version 1.7.3

* Mon Mar 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-1mdv2010.1
+ Revision: 528651
- update to new version 1.7.1

* Sun Dec 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.0-1mdv2010.1
+ Revision: 480446
- fix file list
- update to new version 1.7.0

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-2mdv2010.0
+ Revision: 413197
- rebuild

* Thu Dec 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-1mdv2009.1
+ Revision: 313389
- update to new version 1.6.0
- enable non-blocking communication

* Fri Nov 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.3-1mdv2009.1
+ Revision: 307483
- fix urls
- enable thread-safe functions
- use libgcc when linking
- spec file clean
- update to new version 1.5.3

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.5.2-2mdv2009.0
+ Revision: 266440
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 1.5.2-1mdv2009.0
+ Revision: 213878
- New version 1.5.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sat Nov 24 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.1-1mdv2008.1
+ Revision: 111764
- fix group
- initial package based on Fedora spec, thx! :)
- create c-ares

