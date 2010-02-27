# NOTE: g++ eats 600+MB of memory
Summary:	Image blending with multiresolution splines
Summary(pl.UTF-8):	Łączenie zdjęć przy użyciu splajnów wielokrotnej rozdzielczości
Name:		enblend-enfuse
Version:	3.2
Release:	2
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/enblend/%{name}-%{version}.tar.gz
# Source0-md5:	9b6ebaf672f5103c633a53c9723d99c3
Patch0:		%{name}-opt.patch
URL:		http://enblend.sourceforge.net/
BuildRequires:	OpenEXR-devel >= 1.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	glew-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 5:3.4
BuildRequires:	libtiff-devel
BuildRequires:	libxmi-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Provides:	enblend = %{version}
Obsoletes:	enblend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enblend is a tool for compositing images. Given a set of images that
overlap in some irregular way, Enblend overlays them in such a way
that the seam between the images is invisible, or at least very
difficult to see. Enblend does not line up the images for you. Use a
tool like Hugin to do that.

%description -l pl.UTF-8
Enblend to narzędzie do łączenia zdjęć. Po przekazaniu zbioru zdjęć
nachodzących na siebie w jakiś nieregularny sposób Enblend nakłada je
w taki sposób, że połączenia między zdjęciami są niewidoczne, albo
przynajmniej bardzo trudne do zobaczenia. Enblend nie wyrównuje
zdjęć - do tego można użyć narzędzia takiego jak Hugin.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
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
%attr(755,root,root) %{_bindir}/enfuse
%{_mandir}/man1/enblend.1*
%{_mandir}/man1/enfuse.1*
%{_infodir}/enblend.info*
%{_infodir}/enfuse.info*
%{_infodir}/enfuse-focus-stacking.info*
