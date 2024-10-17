Name:		texlive-inkpaper
Version:	54080
Release:	2
Summary:	A mathematical paper template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inkpaper
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inkpaper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inkpaper.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
InkPaper is designed to write mathematical papers,especially
designed for Mathematics Students. ZJGS students. magazine
editors. NOTICE.This is not a Thesis class.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/inkpaper
%doc %{_texmfdistdir}/doc/latex/inkpaper

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
