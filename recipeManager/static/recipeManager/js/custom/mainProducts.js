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
  if (selectedRow!=-1)
    url=newProductUrl.replace("-1",selectedRow);
  else
    url =newProductUrl;

  $.post(url, $('#mainForm').serialize())
  .done(function(data){
        $('#mainTable').html(data);
        $('#mainModal').modal('hide');
        selectedRow=-1;
  })
  .fail( function(xhr, textStatus, errorThrown) {
        if (errorThrown=="BAD REQUEST")
          $(".modal-body").html(xhr.responseText);
        else
          //TODO: Change the error by a nice Dialog :)
          $(".modal-body").html("ERROR");
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

  $.post(filterProductUrl, $('#filterForm').serialize())
  .done(function(data){

      $(button).find('i').removeClass('fa-refresh fa-spin');
      $(button).find('i').addClass('fa-search');
        $('#mainTable').html(data);
        selectedRow=-1;
  })
  .fail( function(xhr, textStatus, errorThrown) {
      $(button).find('i').removeClass('fa-refresh fa-spin');
      $(button).find('i').addClass('fa-search');
        //TODO: Change the error by a nice dialog :)
    });
}



$(document).ready(function() {
  $('#errorAlert').hide();
});
