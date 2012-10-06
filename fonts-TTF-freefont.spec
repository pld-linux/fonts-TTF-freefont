Summary:	Free UCS scalable fonts in TrueType format
Summary(pl.UTF-8):	Wolnodostępne skalowalne fonty UCS w formacie TrueType
Name:		fonts-TTF-freefont
Version:	20120503
Release:	2
License:	GPL v2
Group:		Fonts
Source0:	http://ftp.gnu.org/gnu/freefont/freefont-ttf-%{version}.zip
# Source0-md5:	879b76d2e3c8003d567b555743f39154
URL:		http://www.gnu.org/software/freefont/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This project aims to provide a set of free scalable fonts covering the
ISO 10646/Unicode UCS (Universal Character Set).

%description -l pl.UTF-8
Celem tego projektu jest udostępnienie zestawu wolnodostępnych fontów
skalowalnych pokrywających zakres uniwersalnego zestawu znaków ISO
10646/Unicode.

%prep
%setup -q -n freefont-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README
%{ttffontsdir}/FreeMono*.ttf
%{ttffontsdir}/FreeSans*.ttf
%{ttffontsdir}/FreeSerif*.ttf
