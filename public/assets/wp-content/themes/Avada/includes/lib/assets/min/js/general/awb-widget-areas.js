/*!
 * AWB Widget Areas - minimal stub
 * Handles dynamic widget area display logic for Avada theme
 */
(function($) {
  'use strict';

  function initWidgetAreas() {
    $('.awb-widget-area').each(function() {
      var $area = $(this);
      // Trigger resize for any dynamic content inside widget areas
      $(window).trigger('resize');
    });
  }

  $(document).ready(function() {
    initWidgetAreas();
  });

  // Re-init on dynamic content render
  $(window).on('fusion-dynamic-content-render', function() {
    initWidgetAreas();
  });

})(jQuery);
