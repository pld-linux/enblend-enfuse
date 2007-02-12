# NOTE: g++ eats 400+MB of memory
Summary:	Image blending with multiresolution splines
Summary(pl.UTF-8):   Łączenie zdjęć przy użyciu splajnów wielokrotnej rozdzielczości
Name:		enblend
Version:	3.0
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/enblend/%{name}-%{version}.tar.gz
# Source0-md5:	f80a12ff91a6122c5ea0d102443929da
URL:		http://enblend.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	boost-devel
BuildRequires:	boost-static_assert-devel
BuildRequires:	glew-devel
BuildRequires:	lcms-devel
BuildRequires:	libstdc++-devel >= 5:3.4
BuildRequires:	libtiff-devel
BuildRequires:	libxmi-devel
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
