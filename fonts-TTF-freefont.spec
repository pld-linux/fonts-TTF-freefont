Summary:	Free True Type fonts
Summary(pl):	Darmowe fonty True Type
Name:		fonts-TTF-freefont
Version:	20031008
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	ftp://ftp.gnu.org/savannah/files/freefont/freefont-ttf.zip
# Source0-md5:	b2c9a6348c7679ef2c8fd66250b5ba36
URL:		http://www.nongnu.org/freefont/
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This package contains very nice and free fonts TTF.

%description -l pl
Ten pakiet zawiera bardzo ³adne i darmowe fonty TTF.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install sfd/*.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README CREDITS AUTHORS ChangeLog
%{ttffontsdir}/*.ttf
