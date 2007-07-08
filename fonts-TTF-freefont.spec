Summary:	Free True Type fonts
Summary(pl.UTF-8):	Darmowe fonty True Type
Name:		fonts-TTF-freefont
Version:	20060126
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	http://download.savannah.nongnu.org/releases/freefont/freefont-ttf-20060126.tar.gz
# Source0-md5:	822aba4e2ed065d9d3ded6e26e495854
URL:		http://www.nongnu.org/freefont/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This package contains very nice and free fonts TTF.

%description -l pl.UTF-8
Ten pakiet zawiera bardzo ładne i darmowe fonty TTF.

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
%doc README CREDITS AUTHORS ChangeLog
%{ttffontsdir}/*.ttf
