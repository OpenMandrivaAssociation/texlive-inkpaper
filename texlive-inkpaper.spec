%global tl_name inkpaper
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A mathematical paper template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inkpaper
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inkpaper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inkpaper.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
InkPaper is designed to write mathematical papers,especially designed
for Mathematics Students. ZJGS students. magazine editors. NOTICE.This
is not a Thesis class.

