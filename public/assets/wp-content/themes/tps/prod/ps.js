var touchIn = ("ontouchstart" in document.documentElement);
var iev = 0;
var ua = window.navigator.userAgent;
var msie = ua.indexOf('MSIE ');
if (msie > 0) {
	iev = parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
}
var trident = ua.indexOf('Trident/');
if (trident > 0) {
	var rv = ua.indexOf('rv:');
	iev = parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
}
var edge = ua.indexOf('Edge/');
if (edge > 0) {
   iev = parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
}
var onw = 0;
if (navigator.onLine) {
    onw = 1;
}
function pl(info) {
	try {
		console.log(info);
	} catch (e) {
		//alert(info); 
	}    
}
/* ------------------ */
jQuery('#B_show_debug').on("click", function() {
  jQuery('#z_debug_page').show();
})
if(jQuery(".z_annonces").length > 0){
  jQuery('.z_annonces').find('img').each(function () {
    var a_offre = jQuery(this).attr('alt').split('|');
    var htm = '<div class="info_offre">';
    if(jQuery("#z_specificites").length == 0){
      htm += '<p class="type_offre">';
      htm += a_offre[0]+'</p>';
    }
    htm += '<p class="type_bien">';
    htm += a_offre[1]+'</p>';
    htm += '<p class="lieu">';
    htm += a_offre[2]+'</p>';
    htm += '<p class="surface_nbp">';
    //surface
    var surf = a_offre[3];
    if(surf > 0){
      htm += '<span class="surface">';
      htm += surf+' m<sup>2</sup></span>';
    }
    //nb pieces
    var nbp = a_offre[4];
    if(nbp > 0){
      htm += ', <span class="nbp">'+nbp+' pièce';
      if(nbp > 1){
        htm += 's';
      }
      htm += '</span>';
    }
    htm += '&nbsp;</p></div>';
    jQuery(this).parent().parent().after(htm);
	})
}

if(jQuery(".B_assurer").length > 0){
  jQuery('.B_assurer').each(function () {
      var bdiv = jQuery(this);
      jQuery(bdiv).click(function() {
        var ca = jQuery(bdiv).attr('id').split('_')[1];
        jQuery('#field_choix_assurance').val(ca);
      });
  })
}
if(jQuery("#z_agence_rs").length > 0){
  var htm = '<span>Suivez-nous</span>';
  jQuery(".fusion-social-networks-wrapper").find('a:first-child').before(htm);
}
if(touchIn){
	if(jQuery("#z_actions_agence").length > 0){
		var za = jQuery('#z_actions_agence');
		jQuery('body').append(za);
		jQuery('#z_actions_agence').addClass('za');
	}
}
/*if(jQuery("#z_guide").length > 0){
  var div = jQuery('#z_guide').find('.fusion-panel').first();
  jQuery(div).find('.panel-heading').find('a').addClass('active');
  jQuery(div).find('.panel-collapse').addClass('in');
 }*/