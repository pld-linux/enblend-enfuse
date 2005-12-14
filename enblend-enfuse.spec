Summary:	Image blending with multiresolution splines
Summary(pl):	£±czenie zdjêæ przy u¿yciu splajnów wielokrotnej rozdzielczo¶ci
Name:		enblend
Version:	2.5
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/enblend/%{name}-%{version}.tar.gz
# Source0-md5:	d760e27fa1fa0395c07cc9d1bb1ea3cc
URL:		http://enblend.sourceforge.net/
BuildRequires:	boost-devel
BuildRequires:	boost-static_assert-devel
BuildRequires:	libstdc++-devel >= 5:3.4
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enblend is a tool for compositing images. Given a set of images that
overlap in some irregular way, Enblend overlays them in such a way
that the seam between the images is invisible, or at least very
difficult to see. Enblend does not line up the images for you. Use a
tool like Hugin to do that.

%description -l pl
Enblend to narzêdzie do ³±czenia zdjêæ. Po przekazaniu zbioru zdjêæ
nachodz±cych na siebie w jaki¶ nieregularny sposób Enblend nak³ada je
w taki sposób, ¿e po³±czenia miêdzy zdjêciami s± niewidoczne, albo
przynajmniej bardzo trudne do zobaczenia. Enblend nie wyrównuje
zdjêæ - do tego mo¿na u¿yæ narzêdzia takiego jak Hugin.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO VIGRA_LICENSE
%attr(755,root,root) %{_bindir}/enblend
%{_mandir}/man1/enblend.1*
