var selectedRow=-1;

function openCreateModal() {

  $('#mainModal').modal('show');
  $('.modal-title').html(newModalTitle);
  $('.modal-body').html('<div class="fluid-container">' +
    '<div class="row">' +
    '<div class="col-lg-12 text-center">' +
    '<i class="fa fa-spinner fa-5x fa-spin"></i>' +
    '</div></div></div>');
  $.ajax({
    url: newProductUrl,
    success: function(result) {
      $(".modal-body").html(result);
    }
  });
}

function openEditModal(){
  if (selectedRow==-1){
    $('#errorAlert').slideDown(500);
    $("#errorAlert").fadeTo(2000, 500).slideUp(500);
    return;
  }

  $('#mainModal').modal('show');
  $('.modal-title').html(newModalTitle);
  $('.modal-body').html('<div class="fluid-container">' +
    '<div class="row">' +
    '<div class="col-lg-12 text-center">' +
    '<i class="fa fa-spinner fa-5x fa-spin"></i>' +
    '</div></div></div>');
  $.ajax({
    url: newProductUrl.replace('-1',selectedRow),
    success: function(result) {
      $(".modal-body").html(result);
    }
  });
}

function openDeleteModal(){
  if (selectedRow==-1){
    $('#errorAlert').slideDown(500);
    $("#errorAlert").fadeTo(2000, 500).slideUp(500);
    return;
  }
  $('#deleteModal').modal('show');
}

function submitForm(button) {
  $(button).prop('disabled','true');
  if (selectedRow!=-1)
    url=newProductUrl.replace("-1",selectedRow);
  else
    url =newProductUrl;

  $.post(url, $('#mainForm').serialize())
  .done(function(data){
        $('#mainTable').html(data);
        $('#mainModal').modal('hide');
        $(button).removeAttr('disabled')
        selectedRow=-1;
  })
  .fail( function(xhr, textStatus, errorThrown) {
        if (errorThrown=="BAD REQUEST"){
          $(".modal-body").html(xhr.responseText);
          $(button).removeAttr('disabled')
        }else{
          bootbox.alert("Problem with connection, please, try again.");
          $(button).removeAttr('disabled')
        }
    });
}

function deleteElement(){
  $.get(deleteProductUrl.replace("-1",selectedRow))
  .done(function(data){
        $('#mainTable').html(data);
        $('#deleteModal').modal('hide');
        selectedRow=-1;
  });
}

function rowClick(row){
    if ($(row).attr('data-id')==selectedRow){
      selectedRow=-1;
      $('#mainTable>tbody>tr').removeClass("info");
      return;
    }

    selectedRow=$(row).attr('data-id');
    $('#mainTable>tbody>tr').removeClass("info");
    $(row).addClass("info");
  }

function filterProduct(button){
  $(button).find('i').removeClass('fa-search');
  $(button).find('i').addClass('fa-refresh fa-spin');
  $(button).prop('disabled','true')

  $.post(filterProductUrl, $('#filterForm').serialize())
  .done(function(data){

      $(button).find('i').removeClass('fa-refresh fa-spin');
      $(button).find('i').addClass('fa-search');
      $(button).removeAttr('disabled')
        $('#mainTable').html(data);
        selectedRow=-1;
  })
  .fail( function(xhr, textStatus, errorThrown) {
      $(button).find('i').removeClass('fa-refresh fa-spin');
      $(button).find('i').addClass('fa-search');
      $(button).removeAttr('disabled')
      bootbox.alert("Problem with connection, please, try again.");
    });
}



$(document).ready(function() {
  $('#errorAlert').hide();
});
