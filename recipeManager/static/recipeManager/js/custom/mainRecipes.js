var selectedRow=-1;
var selectedIngredientRow=-1;
var modalType="";
var currentRecipeId=0;


function openCreateModal() {
  mainModal="newRecipe"
  $('#mainModal').modal('show');
  $('.modal-title').html(newModalTitle);
  $('.modal-body').html('<div class="fluid-container">' +
    '<div class="row">' +
    '<div class="col-lg-12 text-center">' +
    '<i class="fa fa-spinner fa-5x fa-spin"></i>' +
    '</div></div></div>');
  $.ajax({
    url: newRecipeUrl,
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
    url: newRecipeUrl.replace('-1',selectedRow),
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

  if (mainModal=="newRecipe"){
    sendNewRecipeForm(button);
  } else if (mainModal=="newIngredient"){
    sendNewIngredientForm(button);
  }

}

function sendNewRecipeForm(button){
  if (selectedRow!=-1)
    url=newRecipeUrl.replace("-1",selectedRow);
  else
    url =newRecipeUrl;

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

function sendNewIngredientForm(button){
  if (selectedIngredientRow!=-1)
    url=newIngredientUrl.replace("-1",selectedIngredientRow);
  else
    url =newIngredientUrl;
  $("#id_recipe").val(currentRecipeId);

  $.post(url, $('#mainForm').serialize())
  .done(function(data){
        $('#mainTable').html(data);
        $('#mainModal').modal('hide');
        $(button).removeAttr('disabled')
        selectedIngredientRow=-1;
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
  $.get(deleteRecipeUrl.replace("-1",selectedRow))
  .done(function(data){
        $('#mainTable').html(data);
        $('#deleteModal').modal('hide');
        selectedRow=-1;
  });
}

function rowClick(row){
    selectedRow=$(row).attr('data-id');
    $('#mainTable>tbody>tr').removeClass("info");
    $(row).addClass("info");
      url=selectRecipeUrl.replace("-1",selectedRow);
    $.get(url)
    .done(function(data){
          $('#detailPanel').html(data);
    })
    .fail( function(xhr, textStatus, errorThrown) {
        bootbox.alert("Problem with connection, please, try again.");
      });
  }

function filterElements(button){
  $(button).find('i').removeClass('fa-search');
  $(button).find('i').addClass('fa-refresh fa-spin');
  $(button).prop('disabled','true')

  $.post(filterRecipeUrl, $('#filterForm').serialize())
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

function openIngredientModal(){
  $('#mainModal').modal('show');
  $('.modal-title').html(newIngredientModalTitle);
  $('.modal-body').html('<div class="fluid-container">' +
    '<div class="row">' +
    '<div class="col-lg-12 text-center">' +
    '<i class="fa fa-spinner fa-5x fa-spin"></i>' +
    '</div></div></div>');
  $.ajax({
    url: newIngredientUrl.replace("-1",selectedIngredientRow),
    success: function(result) {
      $(".modal-body").html(result);
      $('#id_product').select2();
      mainModal="newIngredient";
    }
  });
}

$(document).ready(function() {
  $('#errorAlert').hide();
  if ($('#mainTable>tbody>tr').length!=0){
    $('#mainTable>tbody>tr:first').addClass("info");
    currentRecipeId=$('#mainTable>tbody>tr:first').attr("data-id");
  }
});
