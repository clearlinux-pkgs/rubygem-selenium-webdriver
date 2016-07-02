#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-selenium-webdriver
Version  : 2.53.4
Release  : 15
URL      : https://rubygems.org/downloads/selenium-webdriver-2.53.4.gem
Source0  : https://rubygems.org/downloads/selenium-webdriver-2.53.4.gem
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
and has been tested to work on MRI (1.9.2 through 2.1),
JRuby and Rubinius.

%package lib
Summary: lib components for the rubygem-selenium-webdriver package.
Group: Libraries

%description lib
lib components for the rubygem-selenium-webdriver package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n selenium-webdriver-2.53.4
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
selenium-webdriver-2.53.4.gem

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
/usr/lib64/ruby/gems/2.3.0/cache/selenium-webdriver-2.53.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/CHANGES
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/README.md
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium-client.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium-webdriver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/driver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/idiomatic.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/javascript_expression_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/javascript_frameworks/jquery.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/javascript_frameworks/prototype.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/legacy_driver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/protocol.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/client/selenium_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/rake/server_task.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/android.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/android/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/chrome.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/chrome/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/chrome/profile.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/chrome/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/action_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/alert.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/bridge_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/core_ext/base64.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/core_ext/dir.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_input_devices.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_location.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_network_connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_remote_status.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_session_id.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_touch_screen.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/has_web_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/rotatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/takes_screenshot.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/driver_extensions/uploads_files.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/element.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/file_reaper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/html5/local_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/html5/location.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/html5/session_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/html5/shared_web_storage.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/keyboard.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/keys.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/log_entry.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/logs.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/mouse.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/navigation.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/platform.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/port_prober.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/profile_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/search_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/socket_lock.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/socket_poller.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/target_locator.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/timeouts.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/touch_action_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/touch_screen.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/w3c_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/wait.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/window.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/common/zipper.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/edge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/edge/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/edge/legacy_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/edge/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/binary.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/extension/prefs.json
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/extension/webdriver.xpi
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/launcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/profile.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/profiles_ini.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/w3c_bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/ie.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/ie/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/ie/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/iphone.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/iphone/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/phantomjs.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/phantomjs/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/phantomjs/service.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/capabilities.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/http/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/http/curb.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/http/default.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/http/persistent.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/response.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/server_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/w3c_bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/w3c_capabilities.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/remote/w3c_commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/safari.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/safari/bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/safari/browser.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/safari/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/safari/resources/client.js
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/safari/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/support.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/support/abstract_event_listener.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/support/block_event_listener.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/support/color.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/support/event_firing_bridge.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/support/select.rb
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/selenium-webdriver.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/selenium-webdriver-2.53.4.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/native/linux/amd64/x_ignore_nofocus.so
/usr/lib64/ruby/gems/2.3.0/gems/selenium-webdriver-2.53.4/lib/selenium/webdriver/firefox/native/linux/x86/x_ignore_nofocus.so
