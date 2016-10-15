#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-selenium-webdriver
Version  : 3.0.0
Release  : 17
URL      : https://rubygems.org/downloads/selenium-webdriver-3.0.0.gem
Source0  : https://rubygems.org/downloads/selenium-webdriver-3.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rubygem-selenium-webdriver-lib
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec

%description
# selenium-webdriver
This gem provides Ruby bindings for WebDriver
and has been tested to work on MRI (2.0 through 2.2),

%package lib
Summary: lib components for the rubygem-selenium-webdriver package.
Group: Libraries

%description lib
lib components for the rubygem-selenium-webdriver package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n selenium-webdriver-3.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-selenium-webdriver.gemspec

%build
export LANG=C
gem build rubygem-selenium-webdriver.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
selenium-webdriver-3.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/selenium-webdriver-3.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/CHANGES
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium-webdriver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/atoms.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/atoms/getAttribute.js
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/chrome.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/chrome/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/chrome/profile.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/chrome/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/action_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/alert.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/bridge_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_input_devices.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_location.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_network_connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_remote_status.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_session_id.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_touch_screen.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/has_web_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/rotatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/takes_screenshot.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/driver_extensions/uploads_files.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/element.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/file_reaper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/html5/local_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/html5/session_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/html5/shared_web_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/keyboard.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/keys.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/log_entry.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/logs.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/mouse.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/navigation.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/platform.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/port_prober.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/profile_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/search_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/socket_lock.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/socket_poller.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/target_locator.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/timeouts.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/touch_action_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/touch_screen.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/w3c_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/wait.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/window.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/common/zipper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/edge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/edge/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/edge/legacy_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/edge/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/binary.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/extension/prefs.json
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/extension/webdriver.xpi
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/launcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/profile.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/profiles_ini.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/w3c_bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/ie.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/ie/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/ie/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/phantomjs.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/phantomjs/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/phantomjs/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/capabilities.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/http/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/http/curb.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/http/default.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/http/persistent.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/response.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/server_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/w3c_bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/w3c_capabilities.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/remote/w3c_commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/safari.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/safari/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/safari/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support/abstract_event_listener.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support/block_event_listener.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support/color.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support/escaper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support/event_firing_bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/support/select.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/selenium-webdriver.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/selenium-webdriver-3.0.0.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/native/linux/amd64/x_ignore_nofocus.so
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-3.0.0/lib/selenium/webdriver/firefox/native/linux/x86/x_ignore_nofocus.so
