/*!
 * Fusion Toggles - minimal stub for accordion/toggle panel functionality
 */
jQuery(document).on('ready fusion-element-render-fusion_accordion fusion-element-render-fusion_toggle', function(e, cid) {
  var $scope = cid ? jQuery('div[data-cid="' + cid + '"]') : jQuery(document);

  $scope.find('.fusion-panel .panel-heading a[data-toggle="collapse"]').on('click', function(evt) {
    evt.preventDefault();
    var target = jQuery(this).attr('data-target') || jQuery(this).attr('href');
    var $target = jQuery(target);
    var $panel = $target.parent('.fusion-panel');
    var $parent = $panel.closest('.panel-group');
    var isOpen = $target.hasClass('in');

    // Close others in the same group
    if (!isOpen && $parent.length) {
      $parent.find('.panel-collapse.in').each(function() {
        jQuery(this).removeClass('in').css('height', '');
        jQuery(this).parent('.fusion-panel').removeClass('open');
        jQuery(this).closest('.fusion-panel').find('[data-toggle="collapse"]').attr('aria-expanded', 'false');
      });
    }

    if (isOpen) {
      $target.removeClass('in').css('height', '');
      $panel.removeClass('open');
      jQuery(this).attr('aria-expanded', 'false');
    } else {
      $target.addClass('in').css('height', '');
      $panel.addClass('open');
      jQuery(this).attr('aria-expanded', 'true');
      // Trigger resize for dynamic content
      setTimeout(function() {
        jQuery(window).trigger('resize');
      }, 350);
    }
  });
});
