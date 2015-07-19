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
  $.post(newProductUrl, $('#mainForm').serialize())
  .done(function(data){
      if(Cookies.get("result")=="ok"){
        $('#mainTable').html(data);
        $('#mainModal').modal('hide');
      } else {
        $(".modal-body").html(data);
      }
  });
}

function rowClick(row){
    selectedRow=$(row).attr('data-id');
    $('#mainTable>tbody>tr').removeClass("info");
    $(row).addClass("info");
  }

$(document).ready(function() {});
