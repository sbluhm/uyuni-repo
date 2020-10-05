%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name underscore.string

Name: %{?scl_prefix}nodejs-underscore.string
Version: 3.3.4
Release: 1%{?dist}
Summary: String manipulation extensions for Underscore
License: MIT
Group: Development/Libraries
URL: http://epeli.github.com/underscore.string/
Source0: https://registry.npmjs.org/underscore.string/-/underscore.string-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(sprintf-js) >= 1.0.3
Requires: npm(sprintf-js) < 2.0.0
Requires: npm(util-deprecate) >= 1.0.2
Requires: npm(util-deprecate) < 2.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package 

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr CHANGELOG.markdown %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr camelize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr capitalize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr chars.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr chop.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr classify.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr clean.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr cleanDiacritics.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr component.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr count.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dasherize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr decapitalize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dedent.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr endsWith.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr escapeHTML.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr exports.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr helper %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr humanize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr include.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr insert.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr isBlank.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr join.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr levenshtein.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lines.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lpad.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lrpad.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ltrim.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr map.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr meteor-post.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr meteor-pre.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr naturalCmp.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr numberFormat.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pad.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr pred.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr prune.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr quote.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr repeat.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr replaceAll.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reverse.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rpad.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rtrim.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr slugify.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr splice.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr sprintf.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr startsWith.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr strLeft.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr strLeftBack.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr strRight.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr strRightBack.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr stripTags.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr succ.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr surround.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr swapCase.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr titleize.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr toBoolean.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr toNumber.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr toSentence.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr toSentenceSerial.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr trim.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr truncate.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr underscored.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr unescapeHTML.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr unquote.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr vsprintf.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr words.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr wrap.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc CONTRIBUTING.markdown
%doc README.markdown

%changelog
