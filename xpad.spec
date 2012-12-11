Name: 	 	xpad
Summary: 	Sticky notepad for GTK+2
Version: 	4.0
Release: 	3
Source:		http://launchpad.net/xpad/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
URL:		https://launchpad.net/xpad/
License:	GPLv3+
Group:		Office
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	intltool
BuildRequires:	pkgconfig(sm)

%description
Xpad is a GTK+2 application that emulates real-life sticky notes. If you
are likely to forget something, open up an xpad and jot it down. It
is easy-to-use, fault-tolerant, and its appearance is customizable.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS TODO ChangeLog
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 4.0-2mdv2011.0
+ Revision: 615729
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 4.0-1mdv2010.1
+ Revision: 466285
- new version 4.0

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.14-5mdv2010.0
+ Revision: 435252
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 2.14-4mdv2009.0
+ Revision: 262657
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Jan 21 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.14-1mdv2008.1
+ Revision: 155869
- new upstream version: 2.14
  (fixes an infinite-loop bug)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 2.13-1mdv2008.1
+ Revision: 116753
- New version 2.13

* Sat Jul 14 2007 Funda Wang <fwang@mandriva.org> 2.12-1mdv2008.0
+ Revision: 51998
- New version
- Import xpad



* Mon Feb 13 2006 Jerome Soyer <saispo@mandriva.org> 2.11-1mdk
- New release 2.11

* Wed Oct 05 2005 Lenny Cartier <lenny@mandriva.com> 2.10-1mdk
- 2.10

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 2.9-1mdk
- 2.9
- configure 2.5
- source URL

* Sat Jun 11 2005 Eskild Hustvedt <eskild@mandriva.org> 2.8-1mdk
- New release 2.8

* Fri Jun 03 2005 Eskild Hustvedt <eskild@mandriva.org> 2.7-1mdk
- New release 2.7
- %%mkrel

* Mon Mar 14 2005 Eskild Hustvedt <eskild@mandrake.org> 2.6-3mdk
- Don't include COPYING (GNU GPL is in the common-licenses package)
- Include ChangeLog

* Sun Mar 13 2005 Eskild Hustvedt <eskild@mandrake.org> 2.6-2mdk
- Don't install Makefile.in.in

* Sun Mar 13 2005 Eskild Hustvedt <eskild@mandrake.org> 2.6-1mdk
- New version 2.6

* Fri Mar 04 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.5-1mdk
- 2.5

* Fri Feb 11 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- from Tom Ph <tpgww@onepost.net> :
	- 2.4
	- requires gtk 2.6
	- use existing 48x48 icon
	- po creation

* Tue Oct 21 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.13-1mdk
- 1.13

* Wed Aug 5 2003 Austin Acton <aacton@yorku.ca> 1.11-1mdk
- 1.11
- new icon locations
- add locales

* Wed Apr 2 2003 Austin Acton <aacton@yorku.ca> 1.10.1-1mdk
- 1.10.1

* Sun Feb 9 2003 Austin Acton <aacton@yorku.ca> 1.9-1mdk
- initial package
