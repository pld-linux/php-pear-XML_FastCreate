%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	FastCreate
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - fast creation of valid XML with DTD control and translation options
Summary(pl):	%{_pearname} - szybkie tworzenie poprawnego XML-u ze sprawdzaniem DTD i opcjami dla t³umaczeñ
Name:		php-pear-%{_pearname}
Version:	0.9
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	25c5496940c8f789b7a8a6bf9dd26aa0
URL:		http://pear.php.net/package/XML_FastCreate/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Key features of this package include:
- Easy way to make valid XML :
     $x->div(
         $x->h1("Example"),
         $x->p("Hello"),
         $x->p(array('class'=>'example'), "World !")
     )

- Option to report DTD errors in your XML :
Use internal tool or external program [ Require XML_DTD package ]

- Use output driver of your choice :
Text : return string
XML_Tree : return XML_Tree object [ Require XML_Tree package ]

- Translate option to quickly transform tags by anothers :
ex: Convert your XML to XHTML :
<news><title>Example</title></news>
to :
<div class="news"><h1>Example</h1></div>

- Include a PHP program to quickly transform HTML to FastCreate syntax.
[ Require XML_HTMLSax package ]

In PEAR status of this package is: %{_status}.

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{dtd,%{_subclass}/tags}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/dtd/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/dtd
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/tags/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/tags

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/dtd/
%{php_pear_dir}/%{_class}/%{_subclass}/
