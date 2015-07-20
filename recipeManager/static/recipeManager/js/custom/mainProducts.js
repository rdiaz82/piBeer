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
  if (selectedRow==-1)
    return;

  $('#mainModal').modal('show');
  $('.modal-title').html(newModalTitle);
  $('.modal-body').html('<div class="fluid-container">' +
    '<div class="row">' +
    '<div class="col-lg-12 text-center">' +
    '<i class="fa fa-spinner fa-5x fa-spin"></i>' +
    '</div></div></div>');
  $.ajax({
    url: newProductUrl+selectedRow+"/",
    success: function(result) {
      $(".modal-body").html(result);
    }
  });
}

function submitForm(button) {

  url=newProductUrl+(selectedRow!=-1?selectedRow:"")+"/";

  $.post(url, $('#mainForm').serialize())
  .done(function(data){
        $('#mainTable').html(data);
        $('#mainModal').modal('hide');
  })
  .fail( function(xhr, textStatus, errorThrown) {
        if (errorThrown=="BAD REQUEST")
          $(".modal-body").html(xhr.responseText);
        else
          //TODO: Change the error by a nice Dialog :)
          $(".modal-body").html("ERROR");
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

$(document).ready(function() {});
